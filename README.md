# yt-download-media
[ [English](README.md) | [PT-BR](./docs/README.pt.md) ]
`yt-download-media` is a tool for downloading videos and audio from YouTube simply and efficiently.

## Features

- Support for video and audio downloads.
- User-friendly interface.
- Integration with the `yt-dlp` library for media processing. (https://github.com/yt-dlp/yt-dlp)

## Requirements

Ensure you have the following installed before using the project:

- Python 3.10 or higher
- `yt-dlp` (installed via `pip`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LucasAvela/yt-download-media.git
   cd yt-download-media
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:

   ```bash
   python main.pyw
   ```

2. Enter the YouTube video URL in the "Video or Playlist URL" field.
3. Enter the output path in the "Output PATH" field.
4. Choose the output format.
5. Wait for the process to finish. The file will be saved in the specified directory.

## Project Structure

```plaintext
yt-download-media/
├── main.pyw            # Main project file
├── downloadManager.py  # Project dependency
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

## Contribution

Contributions are welcome! To contribute:

1. Fork the project.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b my-branch
   ```

3. Make the changes and commit:

   ```bash
   git commit -m "Description of changes"
   ```

4. Push your changes:

   ```bash
   git push origin my-branch
   ```

5. Open a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Made with 💻 by [Lucas Avela](https://github.com/LucasAvela).
