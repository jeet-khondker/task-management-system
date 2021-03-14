import React from 'react'
import SearchIcon from "@material-ui/icons/Search"
import AccountCircleIcon from "@material-ui/icons/AccountCircle"
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import AssignmentIcon from '@material-ui/icons/Assignment';

import styled from "styled-components"

function Header() {
    return (
        <div>
            <Wrapper>

                <LogoWrapper>
                    <Logo>
                        <AssignmentIcon></AssignmentIcon>
                    </Logo>
                    <div>
                        <h2>Task Manager</h2>
                    </div>
                </LogoWrapper>

                <SearchWrapper>
                    <SearchBarWrapper>
                        <SearchIconWrapper />
                        <input type="text" placeholder="Search Task"/>
                    </SearchBarWrapper>
                </SearchWrapper>

                <IconsWrapper>
                    <AccountCircleIcon></AccountCircleIcon>
                    <ExitToAppIcon></ExitToAppIcon>
                </IconsWrapper>

            </Wrapper>
        </div>
    )
}

export default Header

const Wrapper = styled.div
`
    display : grid;
    grid-template-columns : 270px auto 170px;
    border-bottom : 1px solid #d3d3d3;
    height : 70px;
    align-items : center;
`

const LogoWrapper = styled.div
`
    height : 45px;
    display : grid;
    grid-template-columns : 25% auto;
    place-items : center;
`
const Logo = styled.div
`
    display : flex;
    height : 50px;
    justify-content : center;
    align-items : center;
`

const SearchWrapper = styled.div
`
    display : grid;
    place-items : center;
`

const SearchIconWrapper = styled(SearchIcon)
`
    color : #5f6368;
`

const SearchBarWrapper = styled.div
`
    background-color : #f1f3f4;
    width : 100%;
    max-width : 750px;
    display : grid;
    grid-template-columns : 10% auto;
    place-items : center;
    height : 45px;
    border-radius : 5px;

    input {
        width : 100%;
        height : 30px;
        background : none;
        border : none;
        font-size: 18px;

        :focus {
            outline : none;
        }
    }
`

const IconsWrapper = styled.div
`
    margin-left : 10px;
    display : grid;
    grid-template-columns : repeat(2, auto);

    .MuiSvgIcon-root {
        color : #5f6368;
    }
`
