import { useEffect, useState } from "react"
import { getAllMatches } from "../services/requests"
import RoundMatches from "./RoundMatches"


const AllMatches = () => {
    const [rounds, setRounds] = useState([])

    useEffect(() => {
        getAllMatches()
            .then(result => {
                setRounds(result)
            })
    }, [])

    return (
        <div>
            {rounds.map(round => <RoundMatches key={round.roundNumber} info={round}/>)}
        </div>
    )
}

export default AllMatches