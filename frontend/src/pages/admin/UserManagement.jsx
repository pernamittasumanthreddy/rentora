import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { Users, Shield, UserX, CheckCircle, Search } from 'lucide-react';

export default function UserManagement() {
  const { addToast } = useNotification();
  const [users, setUsers] = useState(storageService.getUsers());
  const [search, setSearch] = useState('');

  const handleToggleStatus = (id, currentStatus) => {
    const nextStatus = currentStatus === 'ACTIVE' ? 'SUSPENDED' : 'ACTIVE';
    storageService.updateUserStatus(id, nextStatus);
    setUsers(storageService.getUsers());
    addToast(`User status updated to ${nextStatus}`, 'success');
  };

  const filtered = users.filter(
    (u) =>
      u.name.toLowerCase().includes(search.toLowerCase()) ||
      u.email.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Platform User Directory
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Manage identity KYC records, assign roles, and audit account access
        </p>
      </div>

      <div className="card p-4 bg-white border border-gray-100 rounded-2xl flex items-center shadow-sm">
        <Search className="w-4 h-4 text-gray-400 mr-2" />
        <input
          type="text"
          placeholder="Search by name, email, or role..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full bg-transparent text-xs text-gray-900 focus:outline-none placeholder:text-gray-400"
        />
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">User Profile</th>
                <th className="pb-3 px-3">Assigned Role</th>
                <th className="pb-3 px-3">Operating City</th>
                <th className="pb-3 px-3">Phone</th>
                <th className="pb-3 px-3">Joined Date</th>
                <th className="pb-3 px-3">Status</th>
                <th className="pb-3 px-3 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filtered.map((u) => (
                <tr key={u.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3">
                    <div className="flex items-center space-x-3">
                      <img
                        src={u.avatar || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=100&q=80'}
                        alt=""
                        className="w-8 h-8 rounded-full object-cover border border-gray-200"
                      />
                      <div>
                        <span className="font-bold text-gray-900 block">{u.name}</span>
                        <span className="text-gray-400 text-[10px]">{u.email}</span>
                      </div>
                    </div>
                  </td>
                  <td className="py-4 px-3 font-semibold text-gray-800">
                    <span className="px-2 py-0.5 rounded-md text-[10px] bg-sand-100 border border-gray-200">
                      {u.role.replace('ROLE_', '')}
                    </span>
                  </td>
                  <td className="py-4 px-3 text-gray-600">{u.city || 'Bengaluru'}</td>
                  <td className="py-4 px-3 text-gray-600 font-mono">{u.phone}</td>
                  <td className="py-4 px-3 text-gray-500">{u.createdAt}</td>
                  <td className="py-4 px-3">
                    {u.status === 'ACTIVE' ? (
                      <span className="badge-active text-[10px]">ACTIVE</span>
                    ) : (
                      <span className="badge-cancelled text-[10px]">SUSPENDED</span>
                    )}
                  </td>
                  <td className="py-4 px-3 text-right">
                    {u.role !== 'ROLE_ADMIN' && (
                      <button
                        onClick={() => handleToggleStatus(u.id, u.status)}
                        className={`text-xs font-semibold ${
                          u.status === 'ACTIVE'
                            ? 'text-rose-600 hover:text-rose-700'
                            : 'text-emerald-700 hover:text-emerald-800'
                        }`}
                      >
                        {u.status === 'ACTIVE' ? 'Suspend' : 'Reactivate'}
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
