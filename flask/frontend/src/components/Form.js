import React, {useState, useEffect} from 'react'
import APIService from '../components/APIService'

function Form(props) {
    const [title, setTitle] = useState('')
    const [name, setname] = useState('')
    const [tresc, settresc] = useState('')
    useEffect(() => {
        setTitle(props.blog.title)
        setname(props.blog.name)
        settresc(props.blog.tresc)
    }, [props.blog])

    const updateBlog = () => {
            APIService.UpdateBlog(props.blog.id, {title, tresc, name})
            .then(resp => props.updatedData(resp))
            .catch(error => console.log(error))
            
    }
    const insertBlog = () => {
        APIService.InsertBlog({title, name, tresc})
        .then(resp => props.insertedBlog(resp))
            .catch(error => console.log(error))
    }

    return (
        <div>
            {props.blog ? (
                <div className = "mb-3">
                    <label htmlFor = "title" className = "form-label">Title</label>
                    <input type="text" className = "form-control"  placeholder = "Tutaj wpisz tytuł"
                     value = {title} onChange = {(e) => setTitle(e.target.value)}  />

                    <label htmlFor = "name" className = "form-label">Nazwa</label>
                    <input type="text" className = "form-control" placeholder = "Tutaj wpisz nazwę"
                     value = {name} onChange = {(e) => setname(e.target.value)}/>

                    <label htmlFor = "tresc" className = "form-label">Treść</label>
                    <textarea className="form-control" rows = "5" placeholder = "Tutaj wpisz treść"
                    value = {tresc} onChange = {(e) => settresc(e.target.value)}/>

                    {
                        props.blog.id ?
                    <button onClick = {updateBlog} className = "btn btn-success mt-3">Update</button>
                    :
                    <button onClick = {insertBlog} className = "btn btn-success mt-3">Insert</button>
                    }
                </div>
            ):null}
        </div>
    )
}

export default Form
