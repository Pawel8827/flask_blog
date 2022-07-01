import React from 'react'
import APIService from '../components/APIService';

function BlogList(props) {

    const editBlog = (blog) => {
        props.editBlog(blog)
    }
    const deleteBlog = (blog) =>
        APIService.DeleteBlog(blog.id)
        .then(() => props.deleteBlog(blog))

    return (
        <div>
            
      {props.blogs && props.blogs.map(blog => {
        return (
          <div key = {blog.id}>
            <h2>{blog.title}</h2>
            <p>{blog.tresc}</p>
            <p>{blog.name}</p>
            <p>{blog.data_created}</p>
            <div  className = "row">
                <div className ="col-md-1">
                    <button className = "btn btn-primary"
                    onClick = {() => editBlog(blog)}
                    >Update</button>
                    </div> 
            
                <div className ="col">
                    <button className = "btn btn-danger"
                    onClick = {() => deleteBlog(blog)}
                    >Delete</button>
                    </div> 
            </div>
            <hr/>
          </div>
          
        )   
        })}
        
        </div>
    )
}

export default BlogList
