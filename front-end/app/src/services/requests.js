const apiUrl = 'http://127.0.0.1:8000/api'

async function request(url) {
    const response = await fetch(url)
    const result = await response.json()

    return result
}

export const getAllTeams = () => {
    return request(`${apiUrl}/teams/`)
}

export const getAllMatches = () => {
    return request(`${apiUrl}/all_season_matches_by_rounds/`)
}

export const getSelectedTeam = (id) => {
    return request(`${apiUrl}/teams/${id}`)
}

export const getNextUpcomingMatches = () => {
    return request(`${apiUrl}/next_upcoming_matches/`)
}

export const getGamedayMatches = () => {
    return request(`${apiUrl}/gameday_matches/`)
}
