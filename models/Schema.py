from marshmallow import fields, Schema

class BookSchema(Schema):
	id = fields.Int(dump_only=True)
	title = fields.Str(required=True)
	genre = fields.Str(required=True)
	cast = fields.Str(required=True)
	img = fields.Str(required=True)
	amount = fields.Str(required=True)
	available = fields.Str(required=True)
	qty = fields.Str(required=True)


class StatusSchema(Schema):
	id = fields.Int(dump_only=True)
	request_code = fields.Str(required=True)
	user_id = fields.Str(required=True)
	book_id_requested = fields.Str(required=True)
	requested_date = fields.Str(required=True)
	requested_amount = fields.Str(required=True)
	requested_quantity = fields.Str(required=True)
	status = fields.Str(required=True)
	created_at = fields.Str(required=True)
	updated_at = fields.Str(required=True)

class UserSchema(Schema):
	id = fields.Int(dump_only=True)
	email = fields.Str(required=True)
	firstname = fields.Str(required=True)
	middlename = fields.Str(required=True)
	lastname = fields.Str(required=True)
	address = fields.Str(required=True)
	contact_no = fields.Str(required=True)
	verify = fields.Str(required=True)

class HistorySchema(Schema):
	id = fields.Int(dump_only=True)
	request_code = fields.Str(required=True)
	book_id = fields.Str(required=True)
	user_id = fields.Str(required=True)
	duration = fields.Str(required=True)
	collected = fields.Str(required=True)
	remark = fields.Str(required=True)
	remark_date = fields.Str(required=True)