# SongInsight

SongInsight is a Python application that extracts and displays metadata from audio files. It supports various audio formats such as MP3, FLAC, ALAC, M4A, MP4, OGG, WAV, and WV. The application provides a graphical user interface (GUI) for selecting audio files, viewing their metadata in a table, and exporting the metadata to a text file.

## Features

- Supports multiple audio formats: MP3, FLAC, ALAC, M4A, MP4, OGG, WAV, and WV.
- Displays all available metadata in a sorted table format.
- Metadata keys are displayed in bold.
- Displays the duration of the audio file in hours, minutes, and seconds (h:min:s).
- Allows exporting metadata to a text file.

## Prerequisites

- Python 3.x
- `mutagen` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the `mutagen` library using pip:

   ```sh
   pip install mutagen

## Usage

1.  Clone the repository or download the `song_insight.py` file.
    
2.  Run the script:
    ```sh    
    python song_insight.py` 
    
3.  Use the GUI to select an audio file. The metadata will be displayed in a scrollable table.
    
4.  To export the metadata to a text file, click the "Export Metadata" button.
    

## GUI Overview

-   **Open File Button**: Opens a dialog to select an audio file.
-   **Metadata Table**: Displays metadata in two columns: the first column shows metadata keys in bold, and the second column shows the corresponding values.
-   **Export Metadata Button**: Exports the displayed metadata to a text file named after the audio file.


## Author

**Souleimane ZEGGAI** - [My Portfolio](https://www.souleimane-z.com)


## License

This project is licensed under the MIT License.
