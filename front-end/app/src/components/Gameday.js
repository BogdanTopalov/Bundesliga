import { useEffect, useState } from "react"
import { getGamedayMatches } from "../services/requests"
import Match from "./Match"


const Gameday = () => {
    const [matches, setMatches] = useState([])
    const [roundNumber, setRoundNumber] = useState(Number)

    useEffect(() => {
        getGamedayMatches()
            .then(result => {
                setRoundNumber(result.roundNumber)
                setMatches(result.roundMatches)
            })
    }, [])

    return (
        <div className="round">
            <h2>Round {roundNumber}</h2>
            {matches.map(match => <Match key={match.matchID} info={match} />)}
        </div>
    )
}

export default Gameday