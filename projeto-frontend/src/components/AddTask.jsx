import { useState } from "react";

function AddTask({onAddTaskSubmit}){
    const[title, setTitle] = useState("")
    const[description, setDescription] = useState("")
    return (<div className="space-y-4 p-6 bg-slate-200 rounded-md shadow flex flex-col">
        <input 
            value={title} 
            className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md" 
            type="text" placeholder="Digite o titulo da tarefa"
            onChange={(event) => setTitle(event.target.value)}
            />
        <input 
            value={description} 
            className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md" 
            type="text" 
            placeholder="Digite a descrição da tarefa"
            onChange={(event) => setDescription(event.target.value)} />        
        <button className="bg-slate-500 px-4 py-2 rounded-md font-medium text-white"
            onClick={() => {
                if(title.trim === "" || description.trim === ""){
                    alert("Preencha todos os campos")
                    return
                }
                onAddTaskSubmit(title, description)
                setTitle("")
                setDescription("")
            }}>Adicionar</button>
    </div>)
}

export default AddTask;