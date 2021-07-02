from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# example of database

todo = {"task":[]}

def add(request):

	"""this is an api that adds a new task
	---
	parameters:
		Args:
		
			status(bool): True if done, otherwise False
			taskname(str): The name of the task
			description(str): The description of the task 
	responses:True
		
		succesfully:
			{
				"status": "Ok",
				"added_task":{
				
					"status": "status" ,
					"taskname": "taskname",
					"description": "description"
				}
			}

	"""
	if request.method == 'GET':
		ID = request.GET.get('id',False)
		status = request.GET.get('status',False)
		taskname = request.GET.get('taskname',False)
		description = request.GET.get('description','')
		# print(taskname)
		# print(request.GET.items())
		task={}
		task['taskname']=taskname
		task['status']=status
		task['description']=description


		todo['task'].append(task)
	
	return JsonResponse({'result':True})


		print(taskname)
		error = {}
		if not ID:
			error['error'] = "id not given"
		elif not status:
			error['error'] = "status not given"
		elif not taskname:
			error['error'] = "taskname not given"
		elif not description:
			error['error'] = "description not given"
		else:
			todo['task'].append({"id":ID,"status":status,"taskname":taskname,"description":description})

		if len(error) != 0:
			response = error
		else:
			response = todo['task'][-1]





def update(request):
    """this is an api that updates the old function
    ---
    parameters:
        Args:
            id(int): New task ID
            taskname(str): The name of the task
            description: The description of the task
        Kwargs:
            status(bool): True if done, otherwise False
    responses:
		error:
			{
				"status": "description error."
			}
        
      	succesfully:
		  	{
				"status": "Ok",
				"update_task":{
					"id": ID,
					"status": "status" ,
					"taskname": "taskname",
					"description": "description"
				}
			}

    """
    return 0


def update_status(request):
    """this condition is a variable api
    ---
    parameters:
        Args:
            id(int): New task ID
            status(bool): True if done, otherwise false
        Kwargs:
            taskname(str): The name of the task
            description: The description of the task 
    responses:
      	Error:
			{
				"status": "description error."
			}
        
      	Succesfully:
		  	{
				"status": "Ok",
				"update_task":{
					"id": ID,
					"status": "status" ,
					"taskname": "taskname",
					"description": "description"
				}
			}

    """
    return 0


def get_all(request):
	"""this is the api that gives all ADH
    ---
    parameters:
        None
    responses:
		error:
			{
				"status": "description error."
			}
        
      	succesfully:
		  	{
				"status": "Ok",
				"task":[
					{
						"id": ID,
						"status": "status" ,
						"taskname": "taskname",
						"description": "description"
					},
					. . . . .]
			}

    """

	return JsonResponse(todo)


def remove(request):
	"""this is an api that disables the executed AMA
	---
	parameters:
		id(int): Task ID
	responses:
		error:
			{
				"status": "description error."
			}
		
		succesfully:
			{
				"status": "Ok",
				"remove_task":{
					"id": ID,
					"status": "status" ,
					"taskname": "taskname",
					"description": "description"
				}
			}
	"""
	ID = request.GET.get('id',False)

	if not ID:
		response = {"error":"id not entered"}
	else:
		ID = str(ID)
		k = 0
		for i,task in enumerate(todo['task']):
			task_id = task.get('id',False)
			if ID == task_id:
				k += 1
				idx = i
		if k == 0:
			response = {"error":"id not fount"}
		else:
			response = todo['task'].pop(idx)

	return JsonResponse(response)

def clean_all(request):
	"""
	This method clears all added tasks
	"""
	return 0
