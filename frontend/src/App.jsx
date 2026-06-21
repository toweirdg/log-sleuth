import { useState } from 'react'
import { Sidebar } from './components/Sidebar'
import { Overview } from './pages/Overview'
import { Submit } from './pages/Submit'
import { Explorer } from './pages/Explorer'
import { Stats } from './pages/Stats'

const PAGES = {
  overview: Overview,
  submit:   Submit,
  explorer: Explorer,
  stats:    Stats,
}

export default function App() {
  const [page, setPage] = useState('overview')
  const Page = PAGES[page]

  return (
    <div className="min-h-screen bg-zinc-950">
      <Sidebar active={page} onNav={setPage} />
      <main className="ml-52 p-8">
        <Page onNav={setPage} />
      </main>
    </div>
  )
}
