const VARIANTS = {
  // severity
  critical: 'bg-pink-950 text-pink-300 border border-pink-800',
  high:     'bg-red-950  text-red-300  border border-red-800',
  medium:   'bg-amber-950 text-amber-300 border border-amber-800',
  low:      'bg-blue-950 text-blue-300 border border-blue-800',
  // level
  ERROR:    'bg-red-950  text-red-300  border border-red-800',
  WARNING:  'bg-amber-950 text-amber-300 border border-amber-800',
  INFO:     'bg-blue-950 text-blue-300 border border-blue-800',
  DEBUG:    'bg-zinc-800 text-zinc-400 border border-zinc-700',
  // status
  pending:         'bg-zinc-800 text-zinc-400 border border-zinc-700',
  processed:       'bg-emerald-950 text-emerald-300 border border-emerald-800',
  processed_error: 'bg-red-950 text-red-300 border border-red-800',
}

export function Badge({ value }) {
  if (!value) return <span className="text-zinc-600 text-xs">—</span>
  const cls = VARIANTS[value] ?? 'bg-zinc-800 text-zinc-400 border border-zinc-700'
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${cls}`}>
      {value}
    </span>
  )
}
