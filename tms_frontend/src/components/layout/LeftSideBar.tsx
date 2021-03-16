import React from 'react'

import Badge from "@material-ui/core/Badge"
import Avatar from '@material-ui/core/Avatar'
import { makeStyles, createStyles, Theme, withStyles } from '@material-ui/core/styles'

import { sidebarButtonItems } from "../../data/SidebarButtonItems"

import styled from "styled-components"

// Style : Profile Status Theme Styling
const StyledBadge = withStyles((theme : Theme) => 
    createStyles({
        // Style : Profile Status
        badge : {
            backgroundColor : "#44b700",
            color : "#44b700",
            boxShadow : `0 0 0 2px ${ theme.palette.background.paper }`
        },
    })
)(Badge)

// Style : Component Theme Styling
const useStyles = makeStyles((theme : Theme) => 
    createStyles({

        // Style : Avatar Size
        large : {
            width : theme.spacing(10),
            height : theme.spacing(10),
            fontSize : theme.spacing(5),
        },

    })
)

// Arrow Function : Getting Current Date & Time
const getCurrentDateTime = () => {
    let currentDate = new Date()

    // Calculating Date, Month & Year
    let date = currentDate.getDate()
    let month = currentDate.getMonth() + 1
    let year = currentDate.getFullYear()

    // Calculate Hours, Minutes & Seconds
    let hours = currentDate.getHours()
    let minutes = currentDate.getMinutes()
    let seconds = currentDate.getSeconds()

    return `${ year }-${ month < 10 ? `0${ month }` : `${ month }` }-${ date < 10 ? `0${ date }` : `${ date }` } 
            ${ hours < 10 ? `0${ hours }` : `${ hours }` }:${ minutes < 10 ? `0${ minutes }` : `${ minutes }` }:${ seconds < 10 ? `0${ seconds }` : `${ seconds }` }`
}

const LeftSideBar = () => {

    const classes = useStyles()

    return (
        <Wrapper>

            <WelcomeWrapper>
                <StyledBadge 
                    overlap="circle"
                    anchorOrigin={{
                        vertical : "bottom",
                        horizontal : "right"
                    }}
                    variant="dot"
                >
                    <Avatar className={ classes.large }>J</Avatar>
                </StyledBadge>
                <h3>Welcome, </h3>
                <p>{ getCurrentDateTime() }</p>
                <small>Last Logged In : </small>
            </WelcomeWrapper>

            <SideButtonsWrapper>
                {
                    sidebarButtonItems.map(item => (
                        <SidebarButtonItem key={ item.id }>
                            { item.icon } { item.text } { item.count }
                        </SidebarButtonItem>
                    ))
                }
            </SideButtonsWrapper>
        </Wrapper>
    )
}

export default LeftSideBar

const Wrapper = styled.div
`
    border-right : 1px solid #d3d3d3;
    height : 100vh;
`

const WelcomeWrapper = styled.div
`
    display : grid;
    place-items : center;
    align-items : center;
    height : 175px;
    padding : 0 0 20px 0;

    p {
        font-size : 13px;
    }
`

const SideButtonsWrapper = styled.div
`
    border-top : 1px solid #f5f7f7;
    padding : 20px 0 0 0;
`

const SidebarButtonItem = styled.div
`
    display : grid;
    grid-template-columns : 15% 70% 5%;
    align-items : center;
    color : #3A3B3C;
    padding : 5px 25px;
    margin : 10px 0;
    border-radius : 0 100px 100px 0;
    cursor : pointer;

    :hover {
        background-color : #f5f7f7;
    }
`