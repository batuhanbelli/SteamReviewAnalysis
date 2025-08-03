import customtkinter as ctk
from tkinter import filedialog
import re
import time
import pandas as pd
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Steam Review Download tool")
app.geometry("500x600")

link_label = ctk.CTkLabel(app, text="Steam Game link:")
link_label.pack(pady=5)
link_entry = ctk.CTkEntry(app,width=400)
link_entry.pack()

page_label = ctk.CTkLabel(app, text="Number of Pages to Fetch :  ")
page_label.pack(pady=5)
page_entry = ctk.CTkEntry(app, width=100)
page_entry.insert(0,"10")
page_entry.pack()

column_frame = ctk.CTkFrame(app)
column_frame.pack(pady=10, padx=10, fill="both", expand=True)

column_label= ctk.CTkLabel(column_frame, text="Select the Columns You Want: ")
column_label.pack(anchor="w")

language_label = ctk.CTkLabel(app, text="Review Language: ")
language_label.pack(pady=(10,0))

steam_languages = [
    'all', 'english', 'turkish', 'german', 'french', 'spanish',
    'russian', 'koreana', 'japanese', 'schinese', 'tchinese',
    'portuguese', 'polish', 'danish', 'dutch', 'finnish',
    'hungarian', 'italian', 'norwegian', 'romanian', 'swedish'
]

language_combo = ctk.CTkComboBox(app, values=steam_languages)
language_combo.set('all')
language_combo.pack()

available_columns = [
    'author', 'timestamp_created', 'voted_up', 'votes_up',
    'votes_funny', 'review', 'written_during_early_access'
]


checkbox_vars = {}
for col in available_columns:
    var = ctk.StringVar(value="on")
    cb = ctk.CTkCheckBox(column_frame, text=col, variable=var, onvalue="on", offvalue="off")
    cb.pack(anchor="w", padx=10)
    checkbox_vars[col] = var

def parse_app_id_from_link(url_text):
    pattern = r"app/(\d+)"
    match = re.search(pattern, url_text)
    if match:
        return match.group(1)
    else:
        return None


def get_all_reviews(app_id, page_count,language):
    all_reviews = []
    cursor = '*'
    last_cursor = None
    print(f"{app_id} Fetching reviews for game with ID....")

    for i in range(page_count):
        params = {
            'json': 1,
            'filter': 'all',
            'language': language,
            'day_range': '99999',
            'review_type': 'all',
            'purchase_type': 'all',
            'cursor': cursor
        }

        try:
            response = requests.get(f"https://store.steampowered.com/appreviews/{app_id}", params=params)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

        reviews_on_this_page = data.get('reviews', [])
        if not reviews_on_this_page:
            print("No more reviews found to fetch.")
            break

        if cursor == last_cursor:
            print("Reached end of reviews (cursor repeated).")
            break

        last_cursor = cursor
        all_reviews.extend(reviews_on_this_page)

        cursor = data.get('cursor')

        print(f"Page {i + 1} completed. Total {len(all_reviews)} reviews fetched. Next cursor :  {cursor[:10]}")

        time.sleep(1)

    return all_reviews





def start_process():
    print("Process started")

    steam_link = link_entry.get()
    page_count = int(page_entry.get())
    selected_columns = [col for col, var in checkbox_vars.items() if var.get() == "on"]
    language = language_combo.get()

    print("Selected link: ", steam_link)
    print("Page count: ", page_count)
    print("Selected columns: ", selected_columns)

    app_id = parse_app_id_from_link(steam_link)

    if not app_id:
        print("Invalid link")
        return
    print(f"Found app ID: {app_id}")


    reviews_data = get_all_reviews(app_id, page_count,language)

    df_ham = pd.DataFrame(reviews_data)
    df_temiz = df_ham[selected_columns]


    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Csv files", "*.csv"),("all files", "*.*")])

    if file_path:
        df_temiz.to_csv(file_path, index=False)
        print(f"File saved to: {file_path}")
        status_label.configure(text=f"Success: File saved.")
    else:
        print("User canceled file saving.")
        status_label.configure(text="Process canceled.")


process_button = ctk.CTkButton(app, text="Fetch and download data", command=start_process)
process_button.pack(pady=20)

status_label = ctk.CTkLabel(app, text="Ready")
status_label.pack()

app.mainloop()