import React, { useState } from 'react';
import { ShieldAlert, Scale, CheckCircle2, AlertCircle, ArrowRight } from 'lucide-react';

export default function DisputeResolutionCenter() {
  const [activeFilter, setActiveFilter] = useState('ALL');

  const cases = [
        { caseId: 1001, rentalId: 2001, claim: 'Claim #1', amount: '₹1,200', mediator: 'Arbitrator B', status: 'UNDER_ARBITRATION' },
        { caseId: 1002, rentalId: 2002, claim: 'Claim #2', amount: '₹2,400', mediator: 'Arbitrator C', status: 'UNDER_ARBITRATION' },
        { caseId: 1003, rentalId: 2003, claim: 'Claim #3', amount: '₹3,600', mediator: 'Arbitrator D', status: 'RESOLVED' },
        { caseId: 1004, rentalId: 2004, claim: 'Claim #4', amount: '₹4,800', mediator: 'Arbitrator E', status: 'UNDER_ARBITRATION' },
        { caseId: 1005, rentalId: 2005, claim: 'Claim #5', amount: '₹6,000', mediator: 'Arbitrator F', status: 'UNDER_ARBITRATION' },
        { caseId: 1006, rentalId: 2006, claim: 'Claim #6', amount: '₹7,200', mediator: 'Arbitrator G', status: 'RESOLVED' },
        { caseId: 1007, rentalId: 2007, claim: 'Claim #7', amount: '₹8,400', mediator: 'Arbitrator H', status: 'UNDER_ARBITRATION' },
        { caseId: 1008, rentalId: 2008, claim: 'Claim #8', amount: '₹9,600', mediator: 'Arbitrator I', status: 'UNDER_ARBITRATION' },
        { caseId: 1009, rentalId: 2009, claim: 'Claim #9', amount: '₹10,800', mediator: 'Arbitrator J', status: 'RESOLVED' },
        { caseId: 1010, rentalId: 2010, claim: 'Claim #10', amount: '₹12,000', mediator: 'Arbitrator K', status: 'UNDER_ARBITRATION' },
        { caseId: 1011, rentalId: 2011, claim: 'Claim #11', amount: '₹13,200', mediator: 'Arbitrator L', status: 'UNDER_ARBITRATION' },
        { caseId: 1012, rentalId: 2012, claim: 'Claim #12', amount: '₹14,400', mediator: 'Arbitrator M', status: 'RESOLVED' },
        { caseId: 1013, rentalId: 2013, claim: 'Claim #13', amount: '₹15,600', mediator: 'Arbitrator N', status: 'UNDER_ARBITRATION' },
        { caseId: 1014, rentalId: 2014, claim: 'Claim #14', amount: '₹16,800', mediator: 'Arbitrator O', status: 'UNDER_ARBITRATION' },
        { caseId: 1015, rentalId: 2015, claim: 'Claim #15', amount: '₹18,000', mediator: 'Arbitrator P', status: 'RESOLVED' },
        { caseId: 1016, rentalId: 2016, claim: 'Claim #16', amount: '₹19,200', mediator: 'Arbitrator Q', status: 'UNDER_ARBITRATION' },
        { caseId: 1017, rentalId: 2017, claim: 'Claim #17', amount: '₹20,400', mediator: 'Arbitrator R', status: 'UNDER_ARBITRATION' },
        { caseId: 1018, rentalId: 2018, claim: 'Claim #18', amount: '₹21,600', mediator: 'Arbitrator S', status: 'RESOLVED' },
        { caseId: 1019, rentalId: 2019, claim: 'Claim #19', amount: '₹22,800', mediator: 'Arbitrator T', status: 'UNDER_ARBITRATION' },
        { caseId: 1020, rentalId: 2020, claim: 'Claim #20', amount: '₹24,000', mediator: 'Arbitrator U', status: 'UNDER_ARBITRATION' },
        { caseId: 1021, rentalId: 2021, claim: 'Claim #21', amount: '₹25,200', mediator: 'Arbitrator V', status: 'RESOLVED' },
        { caseId: 1022, rentalId: 2022, claim: 'Claim #22', amount: '₹26,400', mediator: 'Arbitrator W', status: 'UNDER_ARBITRATION' },
        { caseId: 1023, rentalId: 2023, claim: 'Claim #23', amount: '₹27,600', mediator: 'Arbitrator X', status: 'UNDER_ARBITRATION' },
        { caseId: 1024, rentalId: 2024, claim: 'Claim #24', amount: '₹28,800', mediator: 'Arbitrator Y', status: 'RESOLVED' },
        { caseId: 1025, rentalId: 2025, claim: 'Claim #25', amount: '₹30,000', mediator: 'Arbitrator Z', status: 'UNDER_ARBITRATION' },
        { caseId: 1026, rentalId: 2026, claim: 'Claim #26', amount: '₹31,200', mediator: 'Arbitrator A', status: 'UNDER_ARBITRATION' },
        { caseId: 1027, rentalId: 2027, claim: 'Claim #27', amount: '₹32,400', mediator: 'Arbitrator B', status: 'RESOLVED' },
        { caseId: 1028, rentalId: 2028, claim: 'Claim #28', amount: '₹33,600', mediator: 'Arbitrator C', status: 'UNDER_ARBITRATION' },
        { caseId: 1029, rentalId: 2029, claim: 'Claim #29', amount: '₹34,800', mediator: 'Arbitrator D', status: 'UNDER_ARBITRATION' },
        { caseId: 1030, rentalId: 2030, claim: 'Claim #30', amount: '₹36,000', mediator: 'Arbitrator E', status: 'RESOLVED' },
        { caseId: 1031, rentalId: 2031, claim: 'Claim #31', amount: '₹37,200', mediator: 'Arbitrator F', status: 'UNDER_ARBITRATION' },
        { caseId: 1032, rentalId: 2032, claim: 'Claim #32', amount: '₹38,400', mediator: 'Arbitrator G', status: 'UNDER_ARBITRATION' },
        { caseId: 1033, rentalId: 2033, claim: 'Claim #33', amount: '₹39,600', mediator: 'Arbitrator H', status: 'RESOLVED' },
        { caseId: 1034, rentalId: 2034, claim: 'Claim #34', amount: '₹40,800', mediator: 'Arbitrator I', status: 'UNDER_ARBITRATION' },
        { caseId: 1035, rentalId: 2035, claim: 'Claim #35', amount: '₹42,000', mediator: 'Arbitrator J', status: 'UNDER_ARBITRATION' },
        { caseId: 1036, rentalId: 2036, claim: 'Claim #36', amount: '₹43,200', mediator: 'Arbitrator K', status: 'RESOLVED' },
        { caseId: 1037, rentalId: 2037, claim: 'Claim #37', amount: '₹44,400', mediator: 'Arbitrator L', status: 'UNDER_ARBITRATION' },
        { caseId: 1038, rentalId: 2038, claim: 'Claim #38', amount: '₹45,600', mediator: 'Arbitrator M', status: 'UNDER_ARBITRATION' },
        { caseId: 1039, rentalId: 2039, claim: 'Claim #39', amount: '₹46,800', mediator: 'Arbitrator N', status: 'RESOLVED' },
        { caseId: 1040, rentalId: 2040, claim: 'Claim #40', amount: '₹48,000', mediator: 'Arbitrator O', status: 'UNDER_ARBITRATION' },
        { caseId: 1041, rentalId: 2041, claim: 'Claim #41', amount: '₹49,200', mediator: 'Arbitrator P', status: 'UNDER_ARBITRATION' },
        { caseId: 1042, rentalId: 2042, claim: 'Claim #42', amount: '₹50,400', mediator: 'Arbitrator Q', status: 'RESOLVED' },
        { caseId: 1043, rentalId: 2043, claim: 'Claim #43', amount: '₹51,600', mediator: 'Arbitrator R', status: 'UNDER_ARBITRATION' },
        { caseId: 1044, rentalId: 2044, claim: 'Claim #44', amount: '₹52,800', mediator: 'Arbitrator S', status: 'UNDER_ARBITRATION' },
        { caseId: 1045, rentalId: 2045, claim: 'Claim #45', amount: '₹54,000', mediator: 'Arbitrator T', status: 'RESOLVED' },
        { caseId: 1046, rentalId: 2046, claim: 'Claim #46', amount: '₹55,200', mediator: 'Arbitrator U', status: 'UNDER_ARBITRATION' },
        { caseId: 1047, rentalId: 2047, claim: 'Claim #47', amount: '₹56,400', mediator: 'Arbitrator V', status: 'UNDER_ARBITRATION' },
        { caseId: 1048, rentalId: 2048, claim: 'Claim #48', amount: '₹57,600', mediator: 'Arbitrator W', status: 'RESOLVED' },
        { caseId: 1049, rentalId: 2049, claim: 'Claim #49', amount: '₹58,800', mediator: 'Arbitrator X', status: 'UNDER_ARBITRATION' },
        { caseId: 1050, rentalId: 2050, claim: 'Claim #50', amount: '₹60,000', mediator: 'Arbitrator Y', status: 'UNDER_ARBITRATION' },
  ];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <Scale className="w-3.5 h-3.5" />
            <span>Escrow Mediation Court</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Dispute Arbitration &amp; Damage Claim Center
          </h3>
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs">
          <thead>
            <tr className="border-b border-gray-200 bg-sand-50/50 text-gray-500 uppercase">
              <th className="py-3 px-4">Case #</th>
              <th className="py-3 px-4">Rental #</th>
              <th className="py-3 px-4">Claim Classification</th>
              <th className="py-3 px-4">Contested Amount</th>
              <th className="py-3 px-4">Assigned Mediator</th>
              <th className="py-3 px-4">Resolution Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {cases.map(c => (
              <tr key={c.caseId} className="hover:bg-sand-50/50">
                <td className="py-3 px-4 font-mono font-bold text-gray-900">#{c.caseId}</td>
                <td className="py-3 px-4 text-emerald-800">#{c.rentalId}</td>
                <td className="py-3 px-4 text-gray-700">{c.claim}</td>
                <td className="py-3 px-4 font-bold text-forest-900">{c.amount}</td>
                <td className="py-3 px-4 text-gray-600">{c.mediator}</td>
                <td className="py-3 px-4">
                  <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold ${
                    c.status === 'RESOLVED' ? 'bg-emerald-100 text-emerald-800' : 'bg-gold-100 text-gold-800'
                  }`}>
                    {c.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
