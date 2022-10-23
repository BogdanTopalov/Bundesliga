import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { getAllTeams } from "../services/requests"


const AllTeams = () => {
    const [teams, setTeams] = useState([])

    useEffect(() => {
        getAllTeams()
            .then(result => {
                setTeams(result)
            })
    }, [])

    return (
        <div className="teams">
            {teams.map(t =>
                <div key={t.teamID}>
                    <Link to={`/teams/${t.teamID}`}>
                        <img src={t.teamInfo.teamIconURL} alt='img' />
                        <p>{t.teamInfo.teamName}</p>
                        <p>Win/Loss ratio: <strong>{t.teamInfo.winLossRatio}</strong></p>
                    </Link>
                </div>
            )
            }
        </div >
    )
}

export default AllTeams