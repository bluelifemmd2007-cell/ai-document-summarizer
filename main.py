from src.cleaner import clean_text

def main():
    text = input("متن مورد نظر را وارد کنید: ")
    cleaned = clean_text(text)
    print("\n--- متن تمیز شده ---")
    print(cleaned)

if __name__ == "__main__":
    main()
