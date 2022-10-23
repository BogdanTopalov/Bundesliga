import Match from "./Match"


const RoundMatches = ({ info }) => {
    return (
        <div className="round">
            <h2>Round {info.roundNumber}</h2>
            {info.roundMatches.map(match => <Match key={match.matchID} info={match} />)}
        </div>
    )
}

export default RoundMatches