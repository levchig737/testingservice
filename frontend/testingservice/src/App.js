import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import { AuthProvider } from './AuthContext';


class App extends React.Component {
    render() {
        return (
            <div className="wrapper">
                <AuthProvider>
                  <Header />
                 </AuthProvider>
                <Footer/>
            </div>
        );
    }
}

export default App;