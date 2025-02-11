
const todoList = [{
    name : 'wash dishes',
    dueTime : '14-02-2004'
},
    {
        name: 'make dinner',
        dueTime: '14-02-2004'
    }];


function addButton() {
    const getElement = document.querySelector('.putText');
    const name = getElement.value;

    const dateInputElement =  document.querySelector('.js-due-date-input');
    const dueDate = dateInputElement.value;
    todoList.push({name: name,
        dueDate: 'dueDate'});
    console.log(todoList);

    getElement.value = '';

    renderTodoList();
}



function renderTodoList() {
    let todoListHTML = ``;

    for (let i = 0; i < todoList.length; i++) {
        const todoObject = todoList[i];
    const name = todoObject.name;
        const dueTime = todoObject.dueTime;
        const html = `
          <p>
            ${name} ${dueTime }
            <button onclick="
            todoList.splice(${i}, 1);
            renderTodoList();
            ">Delete</button></p> `;
        todoListHTML += html;
    }

    document.querySelector('.js-todo-list').innerHTML = todoListHTML;
}



