use r2r::{std_msgs::msg::String as ROS2String, Context, Node, QosProfile};
use std::time::Duration;

#[tokio::main]
async fn main() {
    let ctx = Context::create().unwrap();
    let mut node = Node::create(ctx, "r2r_pub", "").unwrap();
    let publisher = node
        .create_publisher::<ROS2String>("r2r_pub", QosProfile::default())
        .unwrap();

    let mut timer = node.create_wall_timer(Duration::from_millis(1000)).unwrap();

    tokio::task::spawn_blocking(move || loop {
        node.spin_once(Duration::from_millis(100));
    });

    let mut count = 0;

    loop {
        timer.tick().await.unwrap();

        let msg = ROS2String {
            data: format!("Hello, R2R! {}", count),
        };
        publisher.publish(&msg).unwrap();
        r2r::log_info!("r2r_pub", "Publishing: {}", msg.data);

        count += 1;
    }
}
