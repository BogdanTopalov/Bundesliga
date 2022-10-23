import { useEffect, useState } from "react"
import { getNextUpcomingMatches } from "../services/requests"
import RoundMatches from "./RoundMatches"


const NextUpcomingMatches = () => {
    const [upcomingMatches, setUpcomingMatches] = useState([])
    
    useEffect(() => {
        getNextUpcomingMatches()
            .then(result => {
                setUpcomingMatches(result)
            })
    }, [])

    return(
        <div>
            {upcomingMatches.map(round => <RoundMatches key={round.roundNumber} info={round}/>)}
        </div>
    )
}

export default NextUpcomingMatches