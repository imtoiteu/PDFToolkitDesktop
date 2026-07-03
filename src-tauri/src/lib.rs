use tauri_plugin_dialog::DialogExt;

/// Native "Save As" for the desktop app.
///
/// The web UI produces output as an in-memory Blob and hands it to
/// `downloadFile()` (src/js/utils/helpers.ts). Under Tauri that helper calls
/// this command instead of triggering a browser download, so the user gets a
/// real OS save dialog and picks exactly where the file lands.
///
/// Returns `Ok(true)` if the file was written, `Ok(false)` if the user
/// cancelled the dialog, and `Err(_)` on a genuine write failure.
#[tauri::command]
async fn save_file(
    app: tauri::AppHandle,
    filename: String,
    bytes: Vec<u8>,
) -> Result<bool, String> {
    // blocking_save_file() dispatches the native dialog onto the main/UI
    // thread and blocks this command's worker thread until the user chooses.
    let picked = app
        .dialog()
        .file()
        .set_file_name(&filename)
        .blocking_save_file();

    match picked {
        Some(target) => {
            let path = target.into_path().map_err(|e| e.to_string())?;
            std::fs::write(&path, &bytes).map_err(|e| e.to_string())?;
            Ok(true)
        }
        // User dismissed the dialog — not an error.
        None => Ok(false),
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .invoke_handler(tauri::generate_handler![save_file])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
