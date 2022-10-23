import { Link } from "react-router-dom"


const Match = ({ info }) => {
    return (
        <div className="match">
            <div className="match-date">
                <h3>{info.matchDate}</h3>
            </div>
            <div className="match-info">
                <div className="home-team">
                    <h3>{info.homeTeamName}</h3>
                    <Link to={`/teams/${info.homeTeamID}`}>
                        <img src={info.homeTeamIconURL} alt='img' />
                    </Link>
                </div>
                <h3 className="match-result">{info.homeTeamGoals} : {info.awayTeamGoals}</h3>
                <div className="away-team">
                    <Link to={`/teams/${info.awayTeamID}`}>
                        <img src={info.awayTeamIconURL} alt='img' />
                    </Link>
                    <h3>{info.awayTeamName}</h3>
                </div>
            </div>
            <div className="match-time">
                <h3>{info.matchTime}</h3>
            </div>
        </div>
    )
}

export default Match