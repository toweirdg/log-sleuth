import { useState } from 'react'
import { api } from '../api/client'
import { Badge } from '../components/Badge'
import { Sparkles, Send, CheckCircle } from 'lucide-react'

const EXAMPLES = [
  { message: 'Database connection timeout after 30s — max retries exceeded', level: 'ERROR', service: 'auth-service', host: 'prod-01', metadata: '{"region":"ap-south-1","retry_count":3}' },
  { message: 'Memory usage exceeded 90% threshold on worker node', level: 'WARNING', service: 'ml-worker', host: 'gpu-node-02', metadata: '{"usage_pct":92}' },
  { message: 'User login successful', level: 'INFO', service: 'auth-service', host: 'prod-01', metadata: null },
]

export function Submit() {
  const [form, setForm] = useState({ message: '', level: 'ERROR', service: '', host: '', metadata: '' })
  const [result, setResult] = useState<SubmitResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  function updateField(k, v) {setForm(f => ({ ...f, [k]: v }))
}

  function fillExample() {
    const ex = EXAMPLES[Math.floor(Math.random() * EXAMPLES.length)]
    setForm({ message: ex.message, level: ex.level, service: ex.service, host: ex.host, metadata: ex.metadata ? JSON.stringify(JSON.parse(ex.metadata), null, 2) : '' })
    setResult(null); setError(null)
  }

  async function submit() {
    if (!form.message.trim()) { setError('Message is required'); return }
    setLoading(true); setError(null); setResult(null)
    try {
      let metadata = null
      if (form.metadata.trim()) {
        try { metadata = JSON.parse(form.metadata) }
        catch { setError('Metadata must be valid JSON'); setLoading(false); return }
      }
      const d = await api.submitLog({ message: form.message, level: form.level, service: form.service || null, host: form.host || null, metadata })
      setResult(d)
      setForm(f => ({ ...f, message: '', metadata: '' }))
    } catch (e) { setError(e.message) }
    setLoading(false)
  }

  const INPUT = "w-full bg-zinc-950 border border-zinc-700 rounded-lg px-3 py-2 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-blue-600 transition-colors"

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-xl font-medium text-white">Submit log</h1>
        <p className="text-sm text-zinc-500 mt-0.5">Ingest a log entry — Celery worker processes it asynchronously</p>
      </div>
      <div className="max-w-xl">
        <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-5 space-y-4">
          {error && <div className="bg-red-950 border border-red-800 text-red-300 text-sm px-3 py-2 rounded-lg">{error}</div>}
          <div>
            <label className="text-xs text-zinc-500 block mb-1.5">Message *</label>
            <textarea value={form.message} onChange={e => set('message', e.target.value)} rows={3}
              placeholder="e.g. Database connection timeout after 30s retries"
              className={`${INPUT} resize-none`} />
          </div>
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="text-xs text-zinc-500 block mb-1.5">Level</label>
              <select value={form.level} onChange={e => set('level', e.target.value)} className={INPUT}>
                <option>INFO</option><option>WARNING</option><option>ERROR</option><option>DEBUG</option>
              </select>
            </div>
            <div>
              <label className="text-xs text-zinc-500 block mb-1.5">Service</label>
              <input value={form.service} onChange={e => set('service', e.target.value)} placeholder="auth-service" className={INPUT} />
            </div>
          </div>
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="text-xs text-zinc-500 block mb-1.5">Host</label>
              <input value={form.host} onChange={e => set('host', e.target.value)} placeholder="prod-server-01" className={INPUT} />
          </div>
        </div>
      </div>
    </div>
  </div>
  )};
