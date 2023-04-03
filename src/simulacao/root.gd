extends Node2D
var robot_position = null

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_timer_timeout():
	$HTTPRequest.request('http://127.0.0.1:5000/api/position/last')


func _on_http_request_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	robot_position = json.get_data()
	$x.text = "x: " + str(robot_position['x'])
	$y.text = "y: " + str(robot_position['y'])
	$z.text = "z: " + str(robot_position['z'])
	$r.text = "r: " + str(robot_position['r'])
	$j1.text = "j1: " + str(robot_position['j1'])
	$j2.text = "j2: " + str(robot_position['j2'])
	$j3.text = "j3: " + str(robot_position['j3'])
	$j4.text = "j4: " + str(robot_position['j4'])
	print(robot_position.z / 100 * 0.516)
	$arm.scale = Vector2(robot_position.z / 100 * 0.516 , robot_position.z / 100 * 0.835)
	$arm.position = Vector2(532, 546)
	$arm/tip.rotation = robot_position.r / 100 * 2 * PI
	print(robot_position)
