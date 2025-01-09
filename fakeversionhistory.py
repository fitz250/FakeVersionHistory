import random
import time
from docx import Document
from variables import document_path, input_text

def append_text_to_doc(doc_path, paragraphs):
    try:
        # Load the existing document
        doc = Document(doc_path)
    except Exception as e:
        print(f"Error loading document: {e}")
        return

    for paragraph_text in paragraphs:
        if not paragraph_text.strip():
            continue

        words = paragraph_text.split()
        total_words = len(words)
        appended_words = 0

        while appended_words < total_words:
            # Randomly select the number of words to append (between 10 and 15)
            word_count = random.randint(15, 30)
            chunk = words[appended_words:appended_words + word_count]

            if not chunk:
                break

            # Append the chunk as a new paragraph if it's the first chunk, otherwise continue the last paragraph
            if appended_words == 0:
                doc.add_paragraph(' '.join(chunk))
            else:
                doc.paragraphs[-1].add_run(' ' + ' '.join(chunk))

            appended_words += len(chunk)
            print(f"Appended {len(chunk)} words. Total appended: {appended_words}/{total_words}")

            # Save the document after each update
            try:
                doc.save(doc_path)
            except Exception as e:
                print(f"Error saving document: {e}")
                return

            # Wait for 60 seconds before appending the next chunk
            wait_time = random.randint(120, 300)
            print(f"Waiting for {wait_time} seconds before the next append...")
            time.sleep(wait_time)

    print("Text appending completed.")

append_text_to_doc(document_path, input_text)
