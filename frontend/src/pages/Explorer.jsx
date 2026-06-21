import { useEffect, useState } from 'react'
import { api } from '../api/client'
import { Badge } from '../components/Badge'
import { RefreshCw, Eye, X, ChevronLeft, ChevronRight, Sparkles } from 'lucide-react'

const PAGE = 10
const SELECT = "bg-zinc-950 border border-zinc-700 rounded-lg px-2.5 py-1.5 text-sm text-white focus:outline-none focus:border-blue-600 w-full"

export function Explorer() {
  const [logs, setLogs] = useState([])
  const [page, setPage] = useState(0)
  const [filters, setFilters] = useState({ status: '', level: '', severity: '', service: '', sort_by: 'id' })
  const [loading, setLoading] = useState(false)
  const [detail, setDetail] = useState(null)
  const [detailLoading, setDetailLoading] = useState(false)

  function setF(k, v) { setFilters(f => ({ ...f, [k]: v })); setPage(0) }

  async function load(p = page) {
    setLoading(true)
    try {
      const data = await api.getLogs({ ...filters, limit: PAGE, skip: p * PAGE })
      setLogs(data)
    } catch { setLogs([]) }
    setLoading(false)
  }

  useEffect(() => { load(page) }, [filters, page])

  async function openDetail(id) {
    setDetail('loading'); setDetailLoading(true)
    try { setDetail(await api.getLog(id)) }
    catch { setDetail(null) }
    setDetailLoading(false)
  }

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-xl font-medium text-white">Log explorer</h1>
          <p className="text-sm text-zinc-500 mt-0.5">Browse, filter and inspect processed logs</p>
        </div>
        <button onClick={() => load(page)} className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-zinc-700 text-zinc-400 hover:text-white text-sm transition-colors">
          <RefreshCw size={13} />Refresh
        </button>
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-3 mb-4 grid grid-cols-5 gap-2">
        {[
          { key: 'status', label: 'Status', opts: ['','pending','processed','processed_error'] },
          { key: 'level',  label: 'Level',  opts: ['','ERROR','WARNING','INFO','DEBUG'] },
          { key: 'severity',label:'Severity',opts:['','critical','high','medium','low'] },
          { key: 'sort_by',label: 'Sort by', opts: ['id','created_at','severity','status'] },
        ].map(({ key, label, opts }) => (
          <div key={key}>
            <label className="text-xs text-zinc-500 block mb-1">{label}</label>
            <select value={filters[key]} onChange={e => setF(key, e.target.value)} className={SELECT}>
              {opts.map(o => <option key={o} value={o}>{o || 'All'}</option>)}
            </select>
          </div>
        ))}
        <div>
          <label className="text-xs text-zinc-500 block mb-1">Service</label>
          <input value={filters.service} onChange={e => setF('service', e.target.value)} placeholder="auth-service"
            className={SELECT} />
        </div>
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden mb-4">
        <table className="w-full">
          <thead>
            <tr className="border-b border-zinc-800">
              {['ID','Message','Level','Severity','Service','Status',''].map(h => (
                <th key={h} className="text-left text-xs font-medium text-zinc-500 uppercase tracking-wider px-4 py-3">{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan={7} className="text-center py-12 text-zinc-600 text-sm">Loading...</td></tr>
            ) : null}
        </tbody>
      </table>
    </div>
  </div>
)};