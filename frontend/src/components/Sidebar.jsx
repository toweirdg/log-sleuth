import { LayoutDashboard, Send, List, BarChart2, Activity } from 'lucide-react'

const NAV = [
  { id: 'overview', label: 'Overview',     Icon: LayoutDashboard },
  { id: 'submit',   label: 'Submit log',   Icon: Send },
  { id: 'explorer', label: 'Log explorer', Icon: List },
  { id: 'stats',    label: 'Stats',        Icon: BarChart2 },
]

export function Sidebar({ active, onNav }) {
  return (
    <aside className="fixed top-0 left-0 h-screen w-52 bg-zinc-950 border-r border-zinc-800 flex flex-col z-10">
      <div className="flex items-center gap-2.5 px-4 py-5 border-b border-zinc-800">
        <div className="w-7 h-7 bg-blue-600 rounded-lg flex items-center justify-center flex-shrink-0">
          <Activity size={15} className="text-white" />
        </div>
        <div>
          <p className="text-sm font-medium text-white leading-tight">LogSleuth</p>
          <p className="text-xs text-zinc-600">v1.0.0</p>
        </div>
      </div>
      <nav className="flex-1 p-2 space-y-0.5">
        {NAV.map(({ id, label, Icon }) => (
          <button
            key={id}
            onClick={() => onNav(id)}
            className={`w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors text-left
              ${active === id
                ? 'bg-blue-950 text-blue-400'
                : 'text-zinc-500 hover:bg-zinc-900 hover:text-zinc-300'
              }`}
          >
            <Icon size={16} />
            {label}
          </button>
        ))}
      </nav>
      <div className="p-3 border-t border-zinc-800">
        <div className="flex items-center gap-2 text-xs text-zinc-600">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 flex-shrink-0" />
          localhost:8000
        </div>
      </div>
    </aside>
  )
}
