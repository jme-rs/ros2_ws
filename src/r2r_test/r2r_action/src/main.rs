use r2r::nav2_msgs;

fn main() {
    let ctx = r2r::Context::create().unwrap();
    let mut node = r2r::Node::create(ctx, "r2r_action_client_node", "").unwrap();
    // let client = node.create_action_client<>("r2r_action_client").unwrap();
    println!("Hello, world!");
}
