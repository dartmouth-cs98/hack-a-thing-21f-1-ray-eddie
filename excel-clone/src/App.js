//Credit to https://flaviocopes.com/tutorial-react-spreadsheet 
//Holds the table component
import React from 'react'
import Table from './components/Table'

const App = () =>
  (<div style={{ width: 'max-content' }}>
    <Table x={4} y={4} />
  </div>)

export default App