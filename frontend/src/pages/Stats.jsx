import { useEffect, useState } from 'react'
import { api } from '../api/client'
import { StatCard } from '../components/StatCard'
import { RefreshCw } from 'lucide-react'

export function Stats() {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  async function load() {
    try { setData(await api.getStats()); setError(null) }
    catch (e) { setError(e.message) }
  }

  useEffect(() => { load() }, [])

  const errorRate = data?.total_logs
    ? ((data.error_logs / data.total_logs) * 100).toFixed(1) + '%'
    : '0%'

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-xl font-medium text-white">Stats</h1>
          <p className="text-sm text-zinc-500 mt-0.5">Live summary from /logs/stats</p>
        </div>
        <button onClick={load} className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-zinc-700 text-zinc-400 hover:text-white text-sm transition-colors">
          <RefreshCw size={13} />Refresh
        </button>
      </div>

      {error && <div className="bg-red-950 border border-red-800 text-red-300 text-sm px-4 py-3 rounded-lg mb-4">{error}</div>}

      <div className="grid grid-cols-2 gap-3 max-w-md mb-6">
        <StatCard label="Total logs"  value={data?.total_logs}     color="text-white" />
        <StatCard label="Error logs"  value={data?.error_logs}      color="text-red-400" />
        <StatCard label="Processed"   value={data?.processed_logs}  color="text-emerald-400" />
        <StatCard label="Error rate"  value={errorRate}             color="text-amber-400" />
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-4 max-w-md">
        <p className="text-sm font-medium text-white mb-3">Raw API response</p>
        <pre className="text-xs text-blue-400 font-mono bg-zinc-950 p-3 rounded-lg overflow-auto">
          {data ? JSON.stringify(data, null, 2) : 'Loading...'}
        </pre>
        <p className="text-xs text-zinc-600 mt-2">GET /logs/stats</p>
      </div>
    </div>
  )
}
