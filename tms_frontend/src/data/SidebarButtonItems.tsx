import TotalIcon from '@material-ui/icons/Assignment';
import IncompleteIcon from '@material-ui/icons/AssignmentLate';
import CompleteIcon from '@material-ui/icons/AssignmentTurnedIn';

import Notification from '@material-ui/core/Badge';

export const sidebarButtonItems = 
[
    {
        id : 1,
        icon : <TotalIcon />,
        text : "Total Tasks",
        count : <Notification badgeContent={ 10 } color="primary"></Notification>
    },
    {
        id : 2,
        icon : <IncompleteIcon />,
        text : "Incompleted Tasks",
        count : <Notification badgeContent={ 5 } color="secondary"></Notification>
    },
    {
        id : 3,
        icon : <CompleteIcon />,
        text : "Completed Tasks",
        count : <Notification badgeContent={ 5 } color="primary"></Notification>
    },
]