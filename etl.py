import requests 
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import boto3



load_dotenv()

def extract() -> list[dict]:

# This API extracts data from http://universities.hipolabs.com
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data

def transform(data:dict) -> pd.DataFrame:
    #Transform the dataset into desired structure and filters
    df = pd.DataFrame(data)
    print(f"Total Number of Universities from API: {len(data)}")

    # Filter for universities with "California" in the name
    df = df[df["name"].str.contains("California", case=False, na=False)]
    print(f"Number of universities in California: {len(df)}")


    # Clean and join domains and web_pages lists into comma-separated strings
    df['domains'] = [','.join(map(str, l))for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]

    # Reset index and return selected columns
    df = df.reset_index(drop=True)
    return df[["domains", "country", "web_pages", "name"]]
  

  # Load the transformed data into a PostgresSQL database
# def load(df:pd.DataFrame)->None:
  
    # Fetch database credentials from environment variables
    # PG_USER = os.getenv('PG_USER', 'postgres')
    # PG_PASS = os.getenv('PG_PASS', '')
    # PG_HOST = os.getenv('PG_HOST', 'localhost')
    # PG_PORT = os.getenv('PG_PORT', '5432')
    # PG_NAME = os.getenv('PG_NAME', 'university_database')

        # Construct SQLAlchemy connection string with environment variables
    # db_url = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_NAME}"

    # Create the SQLAlchemy engine to connect to PostgreSQL
    # engine = create_engine(db_url)
    # print("Connecting to the database...")
    # df.to_sql('california_universities', engine, if_exists='replace', index=False)
    # print("Data successfully loaded into PostgreSQL.")


def load_to_s3(df:pd.DataFrame) -> None:
    #Save to locaal csv file first
    csv_file = "california_universities.csv"
    df.to_csv(csv_file, index=False)
    print("CSV saved locally.")

    # Fecth AWS credentials from environment variables
    AWS_ACCESS_KEY= os.getenv('AWS_ACCESS_KEY', '')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', '')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    BUCKET_NAME = os.getenv('S3_BUCKET', '')
    OBJECT_NAME = "california_universities.csv"


    print("Uploading CSV to S3...")

 # Initialize S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
)
   # Upload file
    s3.upload_file(csv_file, BUCKET_NAME, OBJECT_NAME)

    print(f"CSV successfully uploaded to s3://{BUCKET_NAME}/{OBJECT_NAME}")

def main():
    data = extract()
    df = transform(data)
    load_to_s3(df)

    
# def main():
#     data = extract()
#     df = transform(data)
#     load(df)


if __name__ == "__main__":
    main()