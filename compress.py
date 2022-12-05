import gzip
import os
from tqdm import tqdm

# Open the original CSV file for reading
with open('cs.csv', 'rb') as original:
    # Open the gzip-compressed file for writing
    with gzip.open('cs.csv.gz', 'wb') as compressed:
        # Create a progress bar using the tqdm module
        with tqdm(total=os.path.getsize('cs.csv')) as pbar:
            # Read the original file in chunks of 1024 bytes
            for chunk in iter(lambda: original.read(1024), b''):
                # Write the chunk to the gzip-compressed file
                compressed.write(chunk)
                # Update the progress bar
                pbar.update(len(chunk))
