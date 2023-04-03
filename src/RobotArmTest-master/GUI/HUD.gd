extends Control

#use it as node since script alone won't have the editor help

var port

signal servo_manually_moved
signal is_ik_enabled

var _base
var _shoulder
var _elbow
var _wrist
var _gripper
var update = false

func _process(delta):
	if update:
		emit_signal("servo_manually_moved", _base, _shoulder, _elbow, _wrist, _gripper)
#		print(_base)
		update = false
	

func _on_ArmIK_servo_moved(base, shoulder, elbow, wrist, gripper):
	_base = int(base)
	_shoulder = int(shoulder)
	_elbow = int(elbow)
	_wrist = int(wrist)
	_gripper = int(gripper)

func _on_gripper_value_changed(value):
	_gripper = value
	update = true

func _on_wrist_value_changed(value):
	_wrist = value
	update = true

func _on_elbow_value_changed(value):
	_elbow = value
	update = true

func _on_shoulder_value_changed(value):
	_shoulder = value
	update = true

func _on_base_value_changed(value):
	_base = value
	update = true

