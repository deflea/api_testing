# Importacion de modulos
import requests
from helpers import helpers_functions as hf

ENDPOINT = "https://todo.pixegami.io"

# Pytest ejecuta las funciones que empiezan con test_
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_tasks():
    payload = hf.new_task_payload()
    create_task_response = hf.create_task(payload,ENDPOINT)
    assert create_task_response.status_code== 200
    data = create_task_response.json()

    task_id = data["task"]["task_id"]
    get_task_response = hf.get_task(task_id,ENDPOINT)    
    
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    payload = hf.new_task_payload()
    create_task_response = hf.create_task(payload,ENDPOINT)
    task_id = create_task_response.json()["task"]["task_id"]
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content":"updated content",
        "is_done":True
    }
    update_task_response = hf.update_task(new_payload,ENDPOINT)
    assert update_task_response.status_code == 200

    get_task_response = hf.get_task(task_id,ENDPOINT)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]


def test_can_list_tasks():
    #Create N tasks
    n = 3
    payload = hf.new_task_payload()
    for _ in range(n):
        create_task_response = hf.create_task(payload,ENDPOINT)
        assert create_task_response.status_code == 200

    #List tasks and check that there are N items
    user_id = payload["user_id"]
    list_task_response = hf.list_tasks(user_id,ENDPOINT)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    
    tasks = data["tasks"]
    assert len(tasks) == n
    

def test_can_delete_tasks():
    payload = hf.new_task_payload()
    create_task_response = hf.create_task(payload,ENDPOINT)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response = hf.delete_task(task_id,ENDPOINT)
    assert delete_task_response.status_code == 200

    get_task_response = hf.get_task(task_id,ENDPOINT)
    assert get_task_response.status_code == 404

