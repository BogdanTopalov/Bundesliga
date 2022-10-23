import { Link } from "react-router-dom"


const Navigation = () => {
    return (
        <nav>
            <Link to='/teams'>Teams</Link>
            <Link to='/all-matches'>All 2022/2023 Matches</Link>
            <Link to='/upcoming-matches'>Next Upcoming Matches</Link>
            <Link to='/gameday'>Gameday</Link>
        </nav>
    )
}

export default Navigation