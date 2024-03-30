use futures::stream::StreamExt;
use r2r::{std_msgs::msg::String as ROS2String, Context, Node, QosProfile};
use std::time::Duration;

#[tokio::main]
async fn main() {
    let ctx = Context::create().unwrap();
    let mut node = Node::create(ctx, "r2r_sub", "").unwrap();
    let subscriber = node
        .subscribe::<ROS2String>("r2r_pub", QosProfile::default())
        .unwrap();

    tokio::task::spawn_blocking(move || loop {
        node.spin_once(Duration::from_millis(100));
    });

    subscriber
        .for_each(|msg| {
            println!("Received: {}", msg.data);
            futures::future::ready(())
        })
        .await;
}
