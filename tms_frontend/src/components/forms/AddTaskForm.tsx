import React from 'react'

import { createStyles, makeStyles, Theme } from "@material-ui/core"
import TextField from "@material-ui/core/TextField"
import Fab from "@material-ui/core/Fab"

import AddIcon from '@material-ui/icons/Add'

import styled from "styled-components"

const useStyles = makeStyles((theme : Theme) => 
    createStyles({

        textField : {
            display : "flex",
            flexFlow : "row wrap",
            marginLeft : theme.spacing(1),
            marginRight : theme.spacing(1),
            marginBottom : theme.spacing(1),
            alignSelf : "center",
            justifyContent : "space-between",
        },

        addButton : {
            display : "flex",
            flexDirection : "row",
            alignSelf : "center",
            alignItems : "center",
            justifyContent : "center",
            width : "100% !important",
        },

    }),
)

const AddTaskForm = () => {

    const classes = useStyles()

    return (
        <div>
            <Wrapper>
                <h1>Manage Your Tasks</h1>
                <FormWrapper>
                    <InputWrapper>
                        <input type="text" placeholder="Task Title" />
                        <input type="text" placeholder="Task Description" />
                        <TextField
                            id="date"
                            label="Deadline"
                            type="date"
                            defaultValue=""
                            className={ classes.textField }
                            fullWidth
                            InputLabelProps={{
                                shrink : true,
                            }}
                        />
                    </InputWrapper>
                    <Fab variant="extended" color="primary" aria-label="add" size="medium" className={ classes.addButton }>
                        <AddIcon />&emsp;Add Task
                    </Fab>
                </FormWrapper>
            </Wrapper>       
        </div>
    )
}

export default AddTaskForm

const Wrapper = styled.div
`
    display : flex;
    flex-flow : row wrap;
    align-items: center;
    justify-content : space-around;
    padding : 10px 20px;
    height : 300px;
    border-radius : 5px;
`

const FormWrapper = styled.div
`
    border : 1px solid #ccc;
    border-radius : 5px;
    padding : 20px;
    background-color : #f1f3f4;
    margin-top : 10px;
`

const InputWrapper = styled.div
`
    display : flex;
    flex-flow : row wrap;
    justify-content : space-between;
    
    input {
        margin : 10px;
        width : 100%;
        font-size: 20px;
        align-self : center;
        padding : 10px;

        :focus {
            outline : none;
        }
    }
`