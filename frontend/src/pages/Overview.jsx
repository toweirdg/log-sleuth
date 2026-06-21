import { useEffect, useState } from 'react'
import { api } from '../api/client'
import { StatCard } from '../components/StatCard'
import { Badge } from '../components/Badge'
import { RefreshCw, Send } from 'lucide-react'

export function Overview({ onNav }) {
  const [stats, setStats] = useState(null)
  const [recent, setRecent] = useState([])
  const [msg, setMsg] = useState('')
  const [level, setLevel] = useState('ERROR')
  const [service, setService] = useState('')
  const [submitting, setSubmitting] = useState(false)
  const [toast, setToast] = useState(null)

  function showToast(text, ok = true) {
    setToast({ text, ok })
    setTimeout(() => setToast(null), 3000)
  }

  async function load() {
    try {
      const [s, logs] = await Promise.all([
        api.getStats(),
        api.getLogs({ limit: 6, sort_by: 'id' }),
      ])
      setStats(s)
      setRecent(logs)
    } catch {}
  }

  useEffect(() => { load() }, [])

  async function quickSubmit() {
    if (!msg.trim()) return
    setSubmitting(true)
    try {
      const d = await api.submitLog({ message: msg, level, service: service || null, host: null, metadata: null })
      showToast(`Log #${d.id} queued`)
      setMsg('')
      load()
    } catch (e) {
      showToast(e.message, false)
    }
    setSubmitting(false)
  }

  const pending = stats ? (stats.total_logs - stats.processed_logs) : null

  return (
    <div>
      {toast && (
        <div className={`fixed bottom-6 right-6 px-4 py-3 rounded-lg text-sm z-50 border
          ${toast.ok ? 'bg-zinc-900 border-blue-700 text-white' : 'bg-zinc-900 border-red-700 text-red-300'}`}>
          {toast.text}
        </div>
      )}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-xl font-medium text-white">Overview</h1>
          <p className="text-sm text-zinc-500 mt-0.5">Real-time log ingestion and analysis</p>
        </div>
        <button onClick={load} className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-zinc-700 text-zinc-400 hover:text-white hover:border-zinc-500 text-sm transition-colors">
          <RefreshCw size={13} />Refresh
        </button>
      </div>

      <div className="grid grid-cols-4 gap-3 mb-6">
        <StatCard label="Total logs"  value={stats?.total_logs}     color="text-white" />
        <StatCard label="Errors"      value={stats?.error_logs}      color="text-red-400" />
        <StatCard label="Processed"   value={stats?.processed_logs}  color="text-emerald-400" />
        <StatCard label="Pending"     value={pending >= 0 ? pending : null} color="text-amber-400" />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-4">
          <p className="text-sm font-medium text-white mb-3">Recent logs</p>
          {recent.length === 0
            ? <p className="text-zinc-600 text-sm text-center py-8">No logs yet</p>
            : recent.map(l => (
              <div key={l.id} className="flex items-start gap-2.5 py-2 border-b border-zinc-800 last:border-0">
                <div className="w-1.5 h-1.5 rounded-full bg-blue-400 mt-1.5 flex-shrink-0" />
                <div className="flex-1 min-w-0">
                  <p className="text-sm text-zinc-200 truncate">{l.message}</p>
                  <div className="flex items-center gap-2 mt-0.5">
                    <span className="text-xs text-zinc-600">{l.service || 'unknown'}</span>
                    <Badge value={l.status} />
                  </div>
                </div>
                <span className="text-xs text-zinc-600 font-mono flex-shrink-0">#{l.id}</span>
              </div>
            ))
          }
        </div>

        <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-4">
          <p className="text-sm font-medium text-white mb-3">Quick submit</p>
          <div className="space-y-3">
            <div>
              <label className="text-xs text-zinc-500 block mb-1">Message</label>
              <input
                value={msg}
                onChange={e => setMsg(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && quickSubmit()}
                placeholder="e.g. Database connection timeout"
                className="w-full bg-zinc-950 border border-zinc-700 rounded-lg px-3 py-2 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-blue-600 transition-colors"
              />
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div>
                <label className="text-xs text-zinc-500 block mb-1">Level</label>
                <select value={level} onChange={e => setLevel(e.target.value)}
                  className="w-full bg-zinc-950 border border-zinc-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-blue-600">
                  <option>INFO</option><option>WARNING</option><option>ERROR</option><option>DEBUG</option>
                </select>
              </div>
              <div>
                <label className="text-xs text-zinc-500 block mb-1">Service</label>
                <input value={service} onChange={e => setService(e.target.value)} placeholder="auth-service"
                  className="w-full bg-zinc-950 border border-zinc-700 rounded-lg px-3 py-2 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-blue-600" />
              </div>
            </div>
            <button onClick={quickSubmit} disabled={submitting}
              className="w-full flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-lg py-2 text-sm font-medium transition-colors">
              {submitting ? <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" /> : <Send size={14} />}
              Submit log
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
