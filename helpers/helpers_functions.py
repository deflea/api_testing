# ----------------------------------------------------------
import requests
import uuid

# Funciones helpers

def create_task(payload,ENDPOINT):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload,ENDPOINT):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id,ENDPOINT):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id,ENDPOINT):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id,ENDPOINT):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    return  {  
        "content": content,
        "user_id": user_id,
        "is_done": False
    }