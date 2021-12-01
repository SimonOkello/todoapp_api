// TASK LIST
var list_snapshot = []
function showList() {
    const taskBox = document.getElementById('task-box')

    const url = 'https://api-for-todoapp.herokuapp.com/api/tasks/'
    fetch(url)
        .then((resp) => resp.json())
        .then((data) => {
            const tasks = data
            for (const obj in tasks) {
                try {
                    document.getElementById(`data-row-${obj}`).remove()
                } catch (error) {

                }
                var title = `<p class="title-strike"><b>${tasks[obj].title}</b></p>`
                var description = `<span class="description">${tasks[obj].description}</span>`
                if (tasks[obj].complete == true) {
                    title = `<strike class="title-strike"><b>${tasks[obj].title}</b></strike>`
                    description = `<strike class="description">${tasks[obj].description}</strike>`

                }
                const item = `
                    <div id="data-row-${obj}" class="box">
                        <article class="media">
                            <div class="media-left">

                            </div>
                            <div class="media-content">
                                ${title}
                                ${description}
                            </div>
                            <span class="icon is-pulled-right">
                                <a href="#" class="edit-btn">
                                    <i class="fas fa-pen"></i>
                                </a>
                            </span>
                            <span class="icon is-pulled-right">
                                <a href="#" class="delete-btn">
                                    <i class="fas fa-trash"></i>
                                </a>
                            </span>
                        </article>

                    </div>

                    `
                taskBox.innerHTML += item


            }
            // Prevent page refresh  when add/edit task
            if (list_snapshot.length > tasks.length) {
                for (var i = tasks.length; i < list_snapshot.length; i++) {
                    document.getElementById(`data-row-${obj}`).remove()

                }

            }
            list_snapshot = tasks

            // EDIT & DELETE BUTTONS DATA PLUS STRIKE/UNSTRIKE TITLE
            for (const obj in tasks) {
                const editBtn = document.getElementsByClassName('edit-btn')[obj]
                const deleteBtn = document.getElementsByClassName('delete-btn')[obj]
                var title = document.getElementsByClassName('title-strike')[obj]
                editBtn.addEventListener('click', function () {
                    editTask(tasks[obj])
                })
                deleteBtn.addEventListener('click', function () {
                    deleteTask(tasks[obj])
                })
                title.addEventListener('click', function () {
                    strikeUnstrikeTask(tasks[obj])
                })
            }
        })
}
showList()

// ADD TASK
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
const taskForm = document.getElementById('task-form')
var activeItem = null
taskForm.addEventListener('submit', function (e) {
    e.preventDefault()
    var url = 'https://api-for-todoapp.herokuapp.com/api/tasks/'
    var request_method ='POST'

    if (activeItem != null) {
        var url = `https://api-for-todoapp.herokuapp.com/api/tasks/${activeItem.id}/`
        var request_method ='PUT'
        activeItem = null
    }
    var title = document.getElementById('title').value
    var description = document.getElementById('description').value
    fetch(url, {
        method: request_method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'title': title, 'description': description })
    }).then(function (response) {
        showList()
        taskForm.reset()
    })

})
// EDIT TASK
function editTask(item) {
    activeItem = item
    document.getElementById('title').value = activeItem.title
    document.getElementById('description').value = activeItem.description
}

// DELETE TASK
function deleteTask(item) {
    var url = `https://api-for-todoapp.herokuapp.com/api/tasks/${item.id}/`
    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    }).then((response) => {
        showList()
    })
}

// STRIKE & UNSTRIKE TASK
function strikeUnstrikeTask(item) {
    var url = `https://api-for-todoapp.herokuapp.com/api/tasks/${item.id}/`
    item.complete = !item.complete
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'title': item.title, 'description': item.description, 'complete': item.complete })
    }).then((response) => {
        showList()
    })
}