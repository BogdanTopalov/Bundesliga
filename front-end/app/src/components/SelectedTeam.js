import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import { getSelectedTeam } from "../services/requests"
import Match from "./Match"


const SelectedTeam = () => {
    const { teamID } = useParams()

    const [teamInfo, setTeamInfo] = useState({})
    const [teamMatches, setTeamMatches] = useState([])

    useEffect(() => {
        getSelectedTeam(teamID)
            .then(result => {
                setTeamInfo(result.teamInfo)
                setTeamMatches(result.teamMatches)
            })
    }, [teamID])

    return (
        <div className="selectedTeam">
            <h1>{teamInfo.teamName}</h1>
            <img src={teamInfo.teamIconURL} alt='img' />
            <h2>Win/Loss ratio: {teamInfo.winLossRatio}</h2>
            {teamMatches.map(match =>
                <div className="round">
                    <h2>Round {match.matchRound}</h2>
                    <Match key={match.matchID} info={match} />
                </div>
            )}
        </div>
    )
}

export default SelectedTeam