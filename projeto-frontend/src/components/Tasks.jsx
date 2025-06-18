import {ChevronRightIcon, TrashIcon} from "lucide-react"
import { useNavigate } from "react-router-dom"

function Tasks(props){
    console.log(props)
    const navigate = useNavigate()

    function onSeeDetailsClick(task){
        // const route = `/task?title=${task.title}&description=${task.description}`
        const query = new URLSearchParams()
        query.set('title', task.title)
        query.set('description', task.description)
        navigate(`/task?${query.toString()}`)
        
    }
    return(
        <ul className="space-y-4 p-6 bg-slate-200 rounded-md shadow">
            {props.tasks.map((task) => (
                <li key={task.id} className="flex gap-2">
                    <button 
                        onClick={() => props.onTaskClick(task.id)} 
                        className={`bg-slate-400 w-full text-white p-2 rounded-md text-left ${task.isCompleted ? "line-through" : ""}`}
                    >
                        {task.title}                        
                    </button>
                    <button onClick={() => onSeeDetailsClick(task)} className="bg-slate-400 p-2 rounded-md text-white">
                        <ChevronRightIcon/>
                    </button>
                    <button onClick={() => props.onDeleteTaskClick
                        (task.id)}className="bg-slate-400 p-2 rounded-md text-white">
                        <TrashIcon/>
                    </button>
                </li>
            ))}
        </ul>
    )
}

export default Tasks