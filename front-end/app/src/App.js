import './App.css';

import { Routes, Route } from 'react-router-dom'

import AllTeams from './components/AllTeams';
import Navigation from './components/Navigation';
import AllMatches from './components/AllMatches';
import NextUpcomingMatches from './components/NextUpcomingMatches';
import SelectedTeam from './components/SelectedTeam';
import Gameday from './components/Gameday';


function App() {
    return (
        <>
            <Navigation />
            <main>
                <Routes>
                    <Route path='/teams' element={<AllTeams />} />
                    <Route path='/teams/:teamID' element={<SelectedTeam />} />
                    <Route path='/all-matches' element={<AllMatches />} />
                    <Route path='/upcoming-matches' element={<NextUpcomingMatches />} />
                    <Route path='/gameday' element={<Gameday />} />
                </Routes>
            </main>
        </>
    );
}

export default App;
