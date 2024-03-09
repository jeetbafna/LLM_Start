from dotenv import load_dotenv
import os

if __name__ == "__main__":
    print("Hello LangChain")
    load_dotenv()
    print(os.environ["COOL_API_KEY"])
