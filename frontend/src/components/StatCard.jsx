export function StatCard({ label, value, color = 'text-white' }) {
  return (
    <div className="bg-zinc-900 rounded-xl p-4 border border-zinc-800">
      <p className="text-xs font-medium text-zinc-500 uppercase tracking-wider mb-2">
        {label}
      </p>
      <p className={`text-3xl font-medium ${color}`}>
        {value ?? '—'}
      </p>
    </div>
  )
}
