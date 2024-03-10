// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use r2r::{std_msgs::msg::String as StringMsg, Context, Node};
use std::sync::{Arc, Mutex};

#[tauri::command]
fn publish_key_input(
    message: &str,
    publisher: tauri::State<Arc<Mutex<r2r::Publisher<StringMsg>>>>,
) {
    let msg = StringMsg {
        data: message.to_string(),
    };
    publisher.lock().unwrap().publish(&msg).unwrap();
    r2r::log_info!("tauri_key_input", "Published: {}", message);
}

#[tokio::main]
async fn main() {
    let ctx = Context::create().unwrap();
    let mut node = Node::create(ctx, "tauri_key_input", "").unwrap();

    let publisher = Arc::new(Mutex::new(
        node.create_publisher::<StringMsg>("key_input", r2r::QosProfile::default())
            .unwrap(),
    ));

    std::thread::spawn(move || loop {
        node.spin_once(std::time::Duration::from_millis(100));
    });

    tauri::Builder::default()
        .manage(publisher)
        .invoke_handler(tauri::generate_handler![publish_key_input])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
