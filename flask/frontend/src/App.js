import './App.css';
import {useState, useEffect} from 'react';
import BlogList from './components/BlogList';
import Form from './components/Form';

function App() {

  const [blogs, setBlogs] = useState([])
  const [editedBlog, setEditedBlog] = useState(null)

  useEffect (() => {
    fetch('http://127.0.0.1:5000/blog', {
      'method': 'GET',
      headers: {
        'Content-Type': 'applications/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => setBlogs(resp))
    .catch(error => console.log(error))
  },[])
  const editBlog = (blog) => {
    setEditedBlog(blog)
    
  }
  const updatedData = (blog) => {
    const new_blog = blogs.map(my_blog =>{
      if(my_blog.id === blog.id){
        return blog
      } else {
        return my_blog
      }
    })
    setBlogs(new_blog)
  }

  const openForm = () => {
    setEditedBlog({title:'', name:'', tresc:''})
  }

  const insertedBlog = (blog) => {
    const new_blogs = [ ...blogs, blog]
    setBlogs(new_blogs)
  }

  const deleteBlog = (blog) => {
    const new_blogs = blogs.filter(myblog => {
      if(myblog.id === blog.id) {
        return false;
      }
      return true
    })
    setBlogs(new_blogs)
  }

  return (
    <div className="App">
      <div className="row">
        <div className="col">
        <h1>Flask and reactjs kurs</h1>
        </div>
      <div className="col">
        <button
        className= "btn btn-success"
        onClick = {openForm}>
           Insert Blog
        </button>

      </div>
      </div>
      <br/>
      <br/>
      <BlogList blogs = {blogs} editBlog = {editBlog} deleteBlog = {deleteBlog}/>
      {editedBlog ? <Form blog = {editedBlog} updatedData = {updatedData} insertedBlog = {insertedBlog}/> : null}
      
      
    </div> 
  )}

export default App;