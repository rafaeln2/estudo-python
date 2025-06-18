
import { json } from "react-router-dom";
import AddTask from "./components/AddTask"
import Tasks from "./components/Tasks"

import { useEffect, useState } from 'react'

function App(){
//   [
//   {
//     id:1,
//     title:"Estudar programação",
//     description:"Estudar programação para ser um bom programador",
//     isCompleted:false
//   },
//   {
//     id:2,
//     title:"Ler livro",
//     description:"Ler um livro para relaxar",
//     isCompleted:false
//   },
//   {
//     id:3,
//     title:"Ir ao cinema",
//     description:"Ir ao cinema com a namorada",
//     isCompleted:false
//   }
// ]
  const [tasks, setTasks] = useState(
    JSON.parse(localStorage.getItem("tasks")) || []
  )

  function onTaskClick(taskId){
    const newTasks = tasks.map((task) => {
      if(task.id === taskId) {
        return {...task, isCompleted: !task.isCompleted}
      }
      return task;  
      }
    );
    setTasks(newTasks)
  }

  function onDeleteTaskClick(taskId){
    const newTasks = tasks.filter((task) => task.id !== taskId)
    setTasks(newTasks)
  }

  function onAddTaskSubmit(title, description){
    const newTask = {
      id: tasks.length + 1,
      title,
      description,
      isCompleted: false
    }
    setTasks([...tasks, newTask])
  }

  useEffect(() => {
    localStorage.setItem("tasks", JSON.stringify(tasks))
  }, [tasks])
  return (
    <div className="w-screen h-screen bg-slate-500 flex justify-center p6">
      <div className="w-[500px] space-y-4">
        <h1 className="text-3xl text-slate-100 font-bold text-center">Gerenciador de tarefas</h1>
        <AddTask onAddTaskSubmit={onAddTaskSubmit}/>
        <Tasks 
          tasks={tasks} 
          onTaskClick={onTaskClick} 
          onDeleteTaskClick={onDeleteTaskClick}/>
      </div>
    </div>
  )
}
export default App